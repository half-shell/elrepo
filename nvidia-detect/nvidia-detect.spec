Name:    nvidia-detect
Version: 310.40
Release: 1%{?dist}
Group:   Applications/System
License: GPLv2
Summary: NVIDIA graphics card detection utility
URL:     https://github.com/elrepo/packages/tree/master/nvidia-detect

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-build-%(%{__id_u} -n)

Source0:  %{name}-%{version}.tar.bz2

BuildRequires: pciutils-devel >= 2.2.4

%description
A utility to detect NVIDIA graphics cards.

%prep
%setup -q

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}/
%{__install} -p -m 0755 nvidia-detect %{buildroot}%{_bindir}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc COPYING README
%{_bindir}/nvidia-detect

%changelog
* Sat Mar 09 2013 Philip J Perry <phil@elrepo.org> - 310.40-1
- Add support for detection of devices added to 310.40 driver release.
- Add support for detection of Optimus hardware configurations.

* Wed Feb 06 2013 Philip J Perry <phil@elrepo.org> - 310.32-1
- Initial build of the package.